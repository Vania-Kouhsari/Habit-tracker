document.addEventListener("DOMContentLoaded", () => {
    const calendarBody = document.getElementById("calendar-body");
    const monthName = document.getElementById("month-name");
    const prevMonthButton = document.getElementById("prev-month");
    const nextMonthButton = document.getElementById("next-month");
  
    const months = [
      "January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"
    ];
  
    let currentYear = 2025;
    let currentMonth = 0; 

    function generateCalendar(year, month) {
      const firstDay = new Date(year, month, 1).getDay();
      const daysInMonth = new Date(year, month + 1, 0).getDate();
  
      // Clear previous calendar
      calendarBody.innerHTML = "";
  
      let date = 1;
      for (let i = 0; i < 6; i++) {
        const row = document.createElement("tr");
  
        for (let j = 0; j < 7; j++) {
          const cell = document.createElement("td");
  
          if (i === 0 && j < firstDay) {
            cell.classList.add("inactive");
            row.appendChild(cell);
          } else if (date > daysInMonth) {
            break;
          } else {
            cell.textContent = date;
            cell.classList.add("active");

            //Highlighting the completed dates
            if (completedDates.includes(`${year}-${String(month + 1).padStart(2, '0')}-${String(date).padStart(2, '0')}`)){
                cell.style.backgroundColor = habitColor;
            }

            row.appendChild(cell);
            date++;
          }
        }
        calendarBody.appendChild(row);
      }
      monthName.textContent = `${months[month]} ${year}`;
    }
  
    // Event Listeners for Month Navigation
    prevMonthButton.addEventListener("click", () => {
      currentMonth--;
      if (currentMonth < 0) {
        currentMonth = 11;
        currentYear--;
      }
      generateCalendar(currentYear, currentMonth);
    });
  
    nextMonthButton.addEventListener("click", () => {
      currentMonth++;
      if (currentMonth > 11) {
        currentMonth = 0;
        currentYear++;
      }
      generateCalendar(currentYear, currentMonth);
    });

// Initialize Calendar
generateCalendar(currentYear, currentMonth);
});