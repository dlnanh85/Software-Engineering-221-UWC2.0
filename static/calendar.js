const date = new Date();

const renderCalendar = () => {
    date.setDate(1);

    
    const monthDays = document.querySelector(".days");

    const lastDay = new Date(
        date.getFullYear(),
        date.getMonth() + 1,
        0
    ).getDate();

    const prevLastDay = new Date(
        date.getFullYear(),
        date.getMonth(),
        0
    ).getDate();

    const firstDayIndex = date.getDay();

    const lastDayIndex = new Date(
        date.getFullYear(),
        date.getMonth() + 1,
        0
    ).getDay();

    let nextDays = 7 - lastDayIndex - 1;

    // if (nextDays == 0)
    //     nextDays = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate()

    const months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ];

    document.querySelector(".date h1").innerHTML = months[date.getMonth()];

    document.querySelector(".date p").innerHTML = new Date().toDateString();

    let dayCount = 0;
    let days = '<div class="week d-flex justify-content-around">';

    for (let x = firstDayIndex; x > 0; x--) {
        console.log('printing')
        days += `<div class="prev-date d-flex justify-content-center align-items-center">${prevLastDay - x + 1}</div>`;
        dayCount++;
        if (dayCount == 7) {
            dayCount = 0;
            days += '</div>';
            days += '<div class="week d-flex justify-content-around">';
        }
    }

    for (let i = 1; i <= lastDay; i++) {
        if (
            i === new Date().getDate() &&
            date.getMonth() === new Date().getMonth()
        ) {
            days += `<div class="today d-flex justify-content-center align-items-center">${i}</div>`;
        } else {
            days += `<div class="d-flex justify-content-center align-items-center">${i}</div>`;
        }
        dayCount++;
        if (dayCount == 7) {
            dayCount = 0;
            days += '</div>';
            days += '<div class="week d-flex justify-content-around">';
        }
    }

    for (let j = 1; j <= nextDays; j++) {
        days += `<div class="next-date d-flex justify-content-center align-items-center">${j}</div>`;
    }
    monthDays.innerHTML = days;
};

renderCalendar();

document.querySelector(".prev").addEventListener("click", () => {
    date.setMonth(date.getMonth() - 1);
    renderCalendar();
});

document.querySelector(".next").addEventListener("click", () => {
    date.setMonth(date.getMonth() + 1);
    renderCalendar();
});
