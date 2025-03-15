<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>@yield('title', $title)</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
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
                    <form action="{{ route('modul_update', $e->id) }}" method="POST" enctype="multipart/form-data">
                        @csrf
                        @method('PUT')
                        <div class="form-group">
                            <label class="font-weight-bold">Nama Modul</label>
                            <input type="text" name="modul" value="<?= $e->nama; ?>" placeholder="Nama Modul" class="form-control" required>
                        </div>

                        <div class="form-group">
                            <label class="font-weight-bold">Icon Modul</label>
                            <input type="text" name="icon" value="<?= $e->icon; ?>" placeholder="Icon Modul" class="form-control" required>
                        </div>

                        <div class="form-group">
                            <label class="font-weight-bold">Status</label>
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
                            <button type="submit" class="btn btn-md btn-primary">UPDATE</button>
                        </div>

                    </form>
                </div>
            </div>
        </div>
    </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
<script src="https://cdn.ckeditor.com/4.13.1/standard/ckeditor.js"></script>
<script>
    CKEDITOR.replace( 'content' );
</script>
</body>
</html>
