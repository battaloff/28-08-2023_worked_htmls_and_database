$(document).ready(function() {
  // Инициализация DataTable
  var table = $('#dataTable').DataTable({
    paging: false,
    info: false
  });

  // Получение сохраненного значения сортировки из локального хранилища
  var savedSort = localStorage.getItem('tableSort');

  // Восстановление сортировки при загрузке страницы
  if (savedSort) {
    table.order(JSON.parse(savedSort)).draw();
  }

  // Сохранение значения сортировки при изменении
  table.on('order.dt', function() {
    var currentSort = JSON.stringify(table.order());
    localStorage.setItem('tableSort', currentSort);
  });

  // Получение сохраненного значения фильтра из локального хранилища
  var savedValue = localStorage.getItem('filterValue');

   // Добавление фильтра с выпадающим списком к столбцу "Оборудование"
  var select = $('<select class="custom-select"><option value="">Все</option></select>')
    .prependTo('.dataTables_filter')
    .on('change', function() {
      var selectedValue = $(this).val();
      table.column(2).search(selectedValue, true, false).draw(false);

      // Сохранение значения фильтра в локальное хранилище
      localStorage.setItem('filterValue', selectedValue);
    });

  table.column(2).data().unique().sort().each(function(d) {
    select.append('<option value="' + d + '">' + d + '</option>');
  });

  select.css({
    'margin-right': '10px',
    'width': '150px',
    'font-size': '14px'
  });

  // Установка сохраненного значения фильтра, если оно есть
  if (savedValue) {
    select.val(savedValue);
    table.column(2).search(savedValue, true, false).draw(false);
  }
});




// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!           Старое  но работающее        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


//
//
//$(document).ready(function() {
//  // Инициализация DataTable
//  var table = $('#dataTable').DataTable({
//    paging: false,
//    info: false
//  });
//
//  // Получение сохраненного значения фильтра из локального хранилища
//  var savedValue = localStorage.getItem('filterValue');
//
//  // Добавление фильтра с выпадающим списком к столбцу "Оборудование"
//  var select = $('<select class="custom-select"><option value="">Все</option></select>')
//    .prependTo('.dataTables_filter')
//    .on('change', function() {
//      var selectedValue = $(this).val();
//      table.column(2).search(selectedValue, true, false).draw(false);
//
//      // Сохранение значения фильтра в локальное хранилище
//      localStorage.setItem('filterValue', selectedValue);
//    });
//
//  table.column(2).data().unique().sort().each(function(d) {
//    select.append('<option value="' + d + '">' + d + '</option>');
//  });
//
//
//  select.css({
//    'margin-right': '10px',
//    'width': '150px',
//    'font-size': '14px' });
//
//// Установка сохраненного значения фильтра, если оно есть
//if (savedValue) { select.val(savedValue); table.column(2).search(savedValue, true, false).draw(false); } });