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
            <form action="{{ route('submenu_add_action') }}" method="POST" enctype="multipart/form-data">
              @csrf
              <div class="form-group">
                <label><b>Nama Menu - [Nama Modul]</b></label>
                <select name="menu_id" class="form-control select2" required>
                  <option value="">-Pilih-</option>
                  <?php foreach($menu as $key => $v) : ?>
                    <option value="<?= $v->id; ?>">[Menu: <?= $v->menu; ?>] - [Modul: <?= $v->modul; ?>]</option>
                  <?php endforeach; ?>
                </select>
              </div>
              <div class="form-group">
                <label><b>Nama Sub Menu</b></label>
                <input type="text" name="sub_menu" placeholder="Nama Sub Menu" required class="form-control">
              </div>
              <div class="form-group">
                <label><b>Icon Sub Menu</b></label>
                <input type="text" name="icon" placeholder="Icon Sub Menu" class="form-control">
              </div>

              <div class="form-group">
                <label class="font-weight-bold">Hak Akses</label>
                <?php
                $data = $level;
                for($i=0; $i < count($data); $i++) :
                  ?>
                  <div class="form-check">
                    <input type="checkbox" name="hak_akses[]" value="<?= $data[$i]->id; ?>" class="form-check-input" >
                    <label class="form-check-label"><?= $data[$i]->nama; ?></label>
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
