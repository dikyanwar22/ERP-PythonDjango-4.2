<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>@yield('title', $title)</title>
  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <!-- Select2 CSS -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/css/select2.min.css">
</head>
<body style="background: lightgray">

    <div class="container mt-5 mb-5">

    <nav aria-label="breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="#">Home</a></li>
            <li class="breadcrumb-item"><a href="#">Form</a></li>
            <li class="breadcrumb-item active" aria-current="page">@yield('title', $title)</li>
        </ol>
    </nav>

    <div class="row">
        <div class="col-md-12">
            <div class="card border-0 shadow-sm rounded">

                <div class="card-body">
                    <form action="{{ route('menu_update', $e->id) }}" method="POST" enctype="multipart/form-data">
                        @csrf
                    @method('PUT')
                    <div class="form-group">
                      <label><b>Nama Modul</b></label>
                      <select name="modul_id" class="form-control select2" required>
                        <option value="">-Pilih-</option>
                        <?php foreach($modul as $key => $v) : ?>
                        <option value="<?= $v->id; ?>" <?= ($v->id == $e->modul_id) ? 'selected' : ''; ?>><?= $v->nama; ?></option>
                        <?php endforeach; ?>
                      </select>
                    </div>
                    <div class="form-group">
                      <label><b>Tipe</b></label>
                      <select name="tipe" class="form-control" required>
                        <?php $tipe = ['menu','dropdown']; ?>
                        <?php for($i=0; $i < count($tipe); $i++) : ?>
                        <option value="<?= $tipe[$i]; ?>" <?= ($e->tipe == $tipe[$i]) ? 'SELECTED' : ''; ?>><?= $tipe[$i]; ?></option>
                        <?php endfor; ?>
                      </select>
                    </div>
                    <div class="form-group">
                      <label><b>Nama Menu</b></label>
                      <input type="text" name="menu" value="<?= $e->nama; ?>" required class="form-control">
                    </div>
                    <div class="form-group">
                      <label><b>Icon Menu</b></label>
                      <input type="text" name="icon" value="<?= $e->icon; ?>" class="form-control">
                    </div>
                    <div class="form-group">
                        <label><b>Status</b></label>
                        <select name="deleted" class="form-control">
                          <?php
                          $status = [0, 1];
                          for($x = 0; $x < count($status); $x++) : ?>
                            <option value="<?= $status[$x]; ?>" <?= ($status[$x] == $e->deleted) ? 'selected' : ''; ?>>
                              <?= ($status[$x] == '0') ? 'Tampil' : 'Tutup'; ?>
                            </option>
                          <?php endfor; ?>
                        </select>
                      </div>

                      <div class="form-group">
                            <label class="font-weight-bold">Hak Akses</label>
                         <?php
                          $array1 = $level;

                          $string = "$e->level_id";
                          $array2 = explode(',',$string);

                          for ($i = 0; $i < count($array1); $i++) :
                            $isChecked = in_array($array1[$i]->id, $array2) ? 'checked' : '';
                            ?>
                            <div class="form-check">
                            <input name="hak_akses[]" type="checkbox" value="<?= $array1[$i]->id ?>" <?= $isChecked; ?> class="form-check-input">
                            <label class="label"><?= $array1[$i]->nama; ?></label>
                            </div>
                          <?php endfor; ?>
                        </div>

                        <div class="text-center">
                            <button type="reset" class="btn btn-md btn-warning">RESET</button>
                            &ensp;
                            <button type="submit" class="btn btn-md btn-primary">SIMPAN</button>
                        </div>

                    </form>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- jQuery -->
<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
<!-- Bootstrap JS -->
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
<!-- Select2 JS -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/js/select2.min.js"></script>
<script>
$(document).ready(function () {
  $('.select2').select2();
});
</script>
</body>
</html>
