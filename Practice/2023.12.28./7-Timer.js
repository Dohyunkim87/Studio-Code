const days = document.getElementById("days");
const hours = document.getElementById("hours");
const minutes = document.getElementById("minutes");
const seconds = document.getElementById("seconds");

const currentYear = new Date().getFullYear();

const newYearTime = new Date(`January 1 ${currentYear+1} 00:00:00`);

// Update Countdown

function updateCountdowntime(){
    const currentTime = new Date();
    const diff = newYearTime - currentTime;

    const d = Math.floor(diff/1000/60/60/24);  // 남은 밀리초를 불러내서, 천으로나누면초, 60으로 나누면 분, 60으로 나누면 시간, 24로 나누면 일;
    const h = Math.floor(diff/1000/60/60) % 24;
    const m = Math.floor(diff/1000/60) % 60;
    const s = Math.floor(diff/1000) % 60;
    
    days.innerHTML = d;
    hours.innerHTML = h < 10 ? '0' + h : h;
    minutes.innerHTML = m < 10 ? '0' + m : m;
    seconds.innerHTML = s < 10 ? '0' + s : s;
}


setInterval(updateCountdowntime,1000);