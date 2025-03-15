from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.http import HttpResponse
from django.db import connection

def modul(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, nama, icon, uri, group_id, deleted FROM modul ORDER BY nama ASC")
        modul = cursor.fetchall()
    data = {'modul_list': []}

    for row in modul:
        modul_id, nama, icon, uri, group_id, deleted = row
        group_ids = group_id.split(",") if group_id else []
        akses_list = []
        if group_ids:
            with connection.cursor() as cursor:
                cursor.execute("SELECT name FROM auth_group WHERE id IN %s ORDER BY name ASC", [tuple(group_ids)])
                akses_list = [row[0] for row in cursor.fetchall()]

        data['modul_list'].append({
            'id': modul_id,
            'nama': nama,
            'icon': icon,
            'uri': uri,
            'deleted': deleted,
            'akses_list': akses_list
        })
    return render(request, "modules/modul/modul/modul.html", {"modul_list": data["modul_list"]})

def menu(request):
    with connection.cursor() as cursor:
        # Query utama untuk mendapatkan data menu
        cursor.execute("""
            SELECT 
                a.id, a.modul_id, a.nama AS menu, a.icon, a.deleted, 
                a.group_id, a.uri AS file, b.uri AS folder, b.nama AS modul
            FROM menu a
            JOIN modul b ON a.modul_id = b.id
            ORDER BY a.nama ASC
        """)
        menu = cursor.fetchall()

    # Menyusun dictionary dari hasil query
    menu_list = [
        {
            'id': row[0], 'modul_id': row[1], 'menu': row[2], 'icon': row[3], 
            'deleted': row[4], 'group_id': row[5], 'file': row[6], 'folder': row[7], 
            'modul': row[8], 'akses': [], 'modul_nama': ''
        }
        for row in menu
    ]

    akses = {}

    # Nested looping untuk mengambil data akses berdasarkan group_id
    for item in menu_list:
        level_ids = item["group_id"].split(",") if item["group_id"] else []
        akses_list = []
        
        with connection.cursor() as cursor:
            for group_id in level_ids:
                cursor.execute("SELECT name FROM auth_group WHERE id = %s ORDER BY name ASC", [group_id])
                result = cursor.fetchone()
                if result:
                    akses_list.append(result[0])

        akses[item["id"]] = akses_list

    # Menambahkan akses ke masing-masing item menu
    for item in menu_list:
        item["akses"] = akses.get(item["id"], [])

    # Looping tambahan untuk mendapatkan modul_nama
    for item in menu_list:
        with connection.cursor() as cursor:
            cursor.execute("SELECT nama FROM modul WHERE id = %s ORDER BY nama ASC LIMIT 1", [item["modul_id"]])
            result = cursor.fetchone()
            item["modul_nama"] = result[0] if result else ""

    return render(request, "modules/modul/menu/menu.html", {"menu": menu_list})

def sub_menu(request):
    with connection.cursor() as cursor:
        # Query untuk mengambil sub-menu
        cursor.execute("""
            SELECT 
                a.id, a.modul_id, a.nama AS sub_menu, a.icon, a.deleted, 
                a.group_id, a.uri AS `function`, b.uri AS folder, b.nama AS modul
            FROM menu a
            JOIN modul b ON a.modul_id = b.id
            ORDER BY a.nama ASC
        """)
        submenu = cursor.fetchall()

    # Konversi hasil query ke dalam list of dictionaries
    submenu_list = [
        {
            'id': row[0], 'modul_id': row[1], 'sub_menu': row[2], 'icon': row[3], 
            'deleted': row[4], 'group_id': row[5], 'function': row[6], 
            'folder': row[7], 'modul': row[8], 'akses': []
        }
        for row in submenu
    ]

    akses = {}

    # Ambil data akses berdasarkan group_id
    for item in submenu_list:
        level_ids = item["group_id"].split(",") if item["group_id"] else []
        akses_list = []

        with connection.cursor() as cursor:
            for group_id in level_ids:
                cursor.execute("SELECT name FROM auth_group WHERE id = %s ORDER BY name ASC", [group_id])
                result = cursor.fetchone()
                if result:
                    akses_list.append(result[0])

        akses[item["id"]] = akses_list

    # Tambahkan akses ke setiap sub-menu
    for item in submenu_list:
        item["akses"] = akses.get(item["id"], [])

    return render(request, "modules/modul/sub_menu/sub_menu.html", {"sub": submenu_list})










    

def module_user(request):
    level_akses = request.session.get('group_id')
    
    query = """
        SELECT 
            modul.id AS modul_id, modul.nama AS modul_nama, modul.icon AS modul_icon,
            menu.id AS menu_id, menu.nama AS menu_nama, menu.icon AS menu_icon, menu.tipe,
            sub_menu.id AS sub_menu_id, sub_menu.icon AS sub_menu_icon, sub_menu.nama AS sub_menu_nama
        FROM menu
        LEFT JOIN sub_menu ON menu.id = sub_menu.menu_id
        LEFT JOIN modul ON menu.modul_id = modul.id
        WHERE FIND_IN_SET(%s, modul.group_id) > 0 
           OR FIND_IN_SET(%s, menu.group_id) > 0 
           OR FIND_IN_SET(%s, sub_menu.group_id) > 0 
        ORDER BY modul.id ASC, menu.sequence ASC, sub_menu.sequence ASC
    """
    
    with connection.cursor() as cursor:
        cursor.execute(query, [level_akses, level_akses, level_akses])
        menus = cursor.fetchall()
    
    data = {}
    for row in menus:
        modul_id, modul_nama, modul_icon, menu_id, menu_nama, menu_icon, tipe, sub_menu_id, sub_menu_icon, sub_menu_nama = row
        
        if modul_id not in data:
            data[modul_id] = {
                'modul_id': modul_id,
                'modul': modul_nama,
                'modul_icon': modul_icon,
                'menus': {}
            }
        
        if menu_id not in data[modul_id]['menus']:
            data[modul_id]['menus'][menu_id] = {
                'menu_id': menu_id,
                'menu': menu_nama,
                'menu_icon': menu_icon,
                'tipe': tipe,
                'sub_menus': []
            }
        
        if tipe == 'dropdown' and sub_menu_id:
            data[modul_id]['menus'][menu_id]['sub_menus'].append({
                'sub_menu_id': sub_menu_id,
                'sub_menu': sub_menu_nama,
                'sub_menu_icon': sub_menu_icon
            })
    
    for modul in data.values():
        modul['menus'] = list(modul['menus'].values())
    
    return JsonResponse(list(data.values()), safe=False)
    