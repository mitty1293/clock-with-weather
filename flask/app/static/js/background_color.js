// Get the current date and time
const current_dt = new Date();
const current_hour = current_dt.getHours();

if (current_hour >= 19) {
    document.body.style.background = "linear-gradient(to right, #65799b, #5e2563)";
    // document.body.style.backgroundColor = "#808080";
    // document.body.style.backgroundImage = "url('img_tree.png')";
} else if (current_hour >= 16) {
    document.body.style.background = "linear-gradient(to right, #fad961, #f76b1c)";
    // document.body.style.backgroundColor = "#FF9966";
} else if (current_hour >= 10) {
    document.body.style.background = "linear-gradient(to right, #17ead9, #6078ea)";
    // document.body.style.backgroundColor = "#66CCFF";
} else if (current_hour >= 5) {
    document.body.style.background = "linear-gradient(to right, #5b247a, #1bcedf)";
    // document.body.style.backgroundColor = "#99CCFF";
} else {
    document.body.style.background = "linear-gradient(to right, #65799b, #5e2563)";
    // document.body.style.backgroundColor = "#808080";
}
