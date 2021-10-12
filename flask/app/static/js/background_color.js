// ・現在時刻をclock.jsと同様に普通に取得する。
// ・{{data['icon']}}から現在天気を取得する。
// ・以下URLの方法で背景色を変えていく。
// https://www.nishishi.com/javascript-tips/doc-bgcolor.html
// ・できたら、横棒を透過で入れる。（figma参照）

// Get the current date and time
const current_dt = new Date();
const current_hour = current_dt.getHours();

if (current_hour >= 19) {
    document.body.style.backgroundColor = "#808080";
    // document.body.style.backgroundImage = "url('img_tree.png')";
} else if (current_hour >= 16) {
    document.body.style.backgroundColor = "#FF9966";
} else if (current_hour >= 10) {
    document.body.style.backgroundColor = "#66CCFF";
} else if (current_hour >= 5) {
    document.body.style.backgroundColor = "#99CCFF";
} else {
    document.body.style.backgroundColor = "#808080";
}
