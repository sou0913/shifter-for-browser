window.onload=function() {
  var submit_btn = document.getElementById('submit_btn');
  submit_btn.addEventListener('click', validates, {passive: false} );
  function validates(e) {
    var year = document.getElementById('year').value;
    var month = document.getElementById('month').value;
    var members = document.getElementById('members').value;
    var holiday = document.getElementById('holiday').value;
    var at_least = document.getElementById('at_least').value;
    var at_holiday = document.getElementById('at_holiday').value;
    var continuous = document.getElementById('continuous').value;
    var errorMsg = "";
    var re_four = /\d{4}/;
    var re = /[^0-9]/;
    if (year.length < 1) {
      errorMsg += "年を入力してください！\n"
    }
    else if (re.test(year) == true) {
      errorMsg += "年は数字で!\n"
    }
    else if (re_four.test(year) == false) {
      errorMsg += "年の値は4桁の整数で!\n"
    }
    if (month.length < 1) {
      errorMsg += "月を入力してください！\n"
    }
    else if (re.test(month) == true) {
      errorMsg += "月は数字で!\n"
    }
    else if (Number(month) < 1 || Number(month) > 12) {
      errorMsg += "月は1~12の整数で！\n"
    }
    if (members.length < 1) {
      errorMsg += "人数を入力してください！\n";
    }
    else if (re.test(members) == true) {
      errorMsg += "人数は数字で！\n"
    }
    if (holiday.length < 1) {
      errorMsg += "休日数を入力してください！\n";
    }
    else if (re.test(holiday) == true) {
      errorMsg += "休日数は数字で!"
    }
    else if (Number(holiday) < 0 || Number(holiday) > 31) {
      errorMsg += "休日数は0~31で!\n"
    }
    if (at_least.length < 1) {
      errorMsg += "最低人数を入力してください！\n";
    }
    else if (re.test(at_least) == true) {
      errorMsg += "最低人数は数字で！\n";
    }
    else if (Number(at_least) > Number(members)) {
      errorMsg += "最低人数が人数を超えてます！\n";
    }
    if (at_holiday.length < 1) {
      errorMsg += "休日の最低人数を入力してください！\n";
    }
    else if (re.test(at_holiday) == true) {
      errorMsg += "休日の最低人数は数字で！\n"
    }
    else if (Number(at_holiday) > Number(members)) {
      errorMsg += "最低人数が人数を超えてます！\n"
    }
    if (continuous.length < 1) {
      errorMsg += "最大連勤数を入力してください！\n";
    }
    else if (re.test(continuous) == true) {
      errorMsg += "最大連勤数は数字で!\n"
    }
    else if (Number(continuous) < 0 || Number(continuous) > 31) {
      errorMsg += "最大連勤数は0~31で!\n"
    }
    if (errorMsg) {
      e.preventDefault();
      alert(errorMsg);
    }
  }
}