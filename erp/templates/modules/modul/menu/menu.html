<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>@yield('title', $title)</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.css">
</head>
<body style="background: lightgray">

    <div class="container mt-5">
        <div class="row">
            <div class="col-md-12">
                <div class="card border-0 shadow-sm rounded">
                    <div class="card-body">

                    <div style="padding-bottom: 30px;">
                       <ul class="nav nav-tabs">
                              <li class="nav-item">
                                <a class="nav-link" href="{{ route('modul') }}">Modul</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link active" aria-current="page" href="{{ route('menu') }}">Menu</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="{{ route('sub_menu') }}">Sub Menu</a>
                            </li>
                        </ul>
                    </div>

                        <a href="{{ route('menu_add') }}" class="btn btn-md btn-success mb-3">TAMBAH</a>
                        <table class="table table-bordered" id="tabel1">
                            <thead>
                              <tr>
                                <th class="text-center">No</th>
                                <th>File di Controller</th>
                                <th>Menu</th>
                                <th>Akses Level</th>
                                <th>Modul</th>
                                <th>Status</th>
                                <th>Aksi</th>
                              </tr>
                            </thead>
                            <tbody>
                            <?php if($menu->count() > 0) : ?>
                            <?php
                                $no = 1;
                                foreach($menu as $key => $v) :
                                $params_id = base64_encode($v->id);
                                $id = rawurlencode($params_id);
                            ?>
                            <tr>
                                <td class="text-center"><?= $no; ?></td>
                                <td><?= $v->folder; ?> / <b style="color: red"><?= $v->file; ?></b></td>
                                <td><i class="<?= $v->icon; ?>"></i> <?= $v->menu; ?></td>
                                <td>
                                  <?php foreach($akses[$v->id] as $nilai) : ?>
                                  <li><?= $nilai; ?></li>
                                  <?php endforeach; ?>
                              </td>
                              <td><?= $v->modul_nama; ?>
                              </td>
                              <td><?= ($v->deleted == '0') ? 'Tampil' : 'Tutup'; ?></td>
                              <td>
                                  <a href="{{route('menu_edit', $id)}}" class="btn btn-sm btn-primary">Edit</a>
                              </td>
                          </tr>
                          <?php $no++; endforeach; ?>
                              <?php else : ?>
                                  <div class="alert alert-danger">
                                      Data Post belum Tersedia.
                                  </div>
                              <?php endif; ?>
                            </tbody>
                          </table>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.js"></script>

    <script>
        //message with toastr
        @if(session()->has('success'))

            toastr.success('{{ session('success') }}', 'BERHASIL!');

        @elseif(session()->has('error'))

            toastr.error('{{ session('error') }}', 'GAGAL!');

        @endif
    </script>

    <!-- Custom Datatables -->
<script src="https://code.jquery.com/jquery-3.1.0.js"></script>
<script src="//cdn.datatables.net/1.10.12/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/1.13.7/js/dataTables.bootstrap5.min.js"></script>
<script>
    $(document).ready(function(){
        $('#tabel1').DataTable();
        $('#tabel2').DataTable();
        $('#tabel3').DataTable();
        $('#tabel4').DataTable();
        $('#tabel5').DataTable();
    });
</script>
<!-- Custom Datatables -->

</body>
</html>
