const clock = () => {
    // Get the current date and time
    const current_dt = new Date();

    // Get elements from current date and time
    let year = current_dt.getFullYear();
    let month = current_dt.getMonth() + 1;
    let date = current_dt.getDate();
    const weekday = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
    let day = weekday[current_dt.getDay()];
    let hour = current_dt.getHours();
    let min = current_dt.getMinutes();
    let sec = current_dt.getSeconds();

    // If it is a single digit, fill it with 0 to make it a double digit
    month = month < 10 ? "0" + month : month;
    date = date < 10 ? "0" + date : date;
    hour = hour < 10 ? "0" + hour : hour;
    min = min < 10 ? "0" + min : min;
    sec = sec < 10 ? "0" + sec : sec;

    // Create a date and time string
    let today = `${year}/${month}/${date} ${day}`;
    let time = `${hour}:${min}:${sec}`;

    document.querySelector(".clock_today").innerText = today;
    document.querySelector(".clock_time").innerText = time;
};

setInterval(clock, 1000);