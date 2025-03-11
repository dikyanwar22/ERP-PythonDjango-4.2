from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django.utils.timezone import now
import logging

# Konfigurasi logging
logging.basicConfig(level=logging.DEBUG, filename='debug.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

def helpdesk_in(request):
    try:
        current_user_id = request.session.get('user_id')
        level_id = request.session.get('group_id')
        
        # Logging untuk debugging
        logging.debug(f"Current User ID: {current_user_id}, Level ID: {level_id}")
        
        if not current_user_id or not level_id:
            return JsonResponse({'error': 'Session data is missing'}, status=400)
        
        query = """
            SELECT a.id, c.first_name AS sender, a.message, a.created_at 
            FROM helpdesk_inbox AS a
            JOIN auth_user AS c ON a.user_id_sender = c.id
            WHERE a.status != '2' AND (
                (a.user_id_receiver IS NOT NULL AND a.user_id_receiver = %s) OR
                (a.user_id_receiver IS NULL AND a.group_id = %s)
            )
            ORDER BY a.id DESC
        """
        
        with connection.cursor() as cursor:
            cursor.execute(query, [current_user_id, level_id])
            result = cursor.fetchall()
        
        # Logging hasil query
        logging.debug(f"Executed Query: {query} | Params: {current_user_id}, {level_id}")
        logging.debug(f"Query Result: {result}")
        
        total = 0
        data = []
        for row in result:
            row_id, sender, message, created_at = row
            total += 1  # Menghitung jumlah data yang ditemukan
            waktu_str = created_at.strftime('%Y-%m-%d %H:%M:%S') if created_at else 'Unknown time'
            data.append({
                'url': "",
                'image': 'https://static-00.iconduck.com/assets.00/user-icon-1024x1024-dtzturco.png',
                'name': sender,
                'helpdesk': message[:40] + '...' if len(message) > 40 else message,
                'waktu': waktu_str,
            })
        
        return JsonResponse({'message': "Data found", 'data': data, 'total': total}, status=200)
    
    except Exception as e:
        logging.error(f"Error in helpdesk_in function: {str(e)}")
        return JsonResponse({'error': 'An error occurred while processing the request.', 'message': str(e)}, status=500)
