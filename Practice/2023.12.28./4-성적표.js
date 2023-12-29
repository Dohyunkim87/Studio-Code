let isShowing75Plus = false;

        function toggleStudents() {
            const rows = document.getElementById("resultBody").getElementsByTagName("tr");
            isShowing75Plus = !isShowing75Plus;

            for (let i = 0; i < rows.length; i++) {
                const score = parseInt(rows[i].getElementsByTagName("td")[1].innerText);
                if (isShowing75Plus) {
                    if (score < 75) {
                        rows[i].style.display = "none";
                    } else {
                        rows[i].style.display = "";
                    }
                    document.getElementById("sortAsc").style.display = "inline-block";
                    document.querySelector('button').textContent = '전체 보기'; // 버튼 텍스트 변경
                } else {
                    rows[i].style.display = "";
                    document.getElementById("sortAsc").style.display = "none";
                    document.querySelector('button').textContent = '75점 넘는 사람만 보기'; // 버튼 텍스트 변경
                }
            }
        }

        function sortAscending() {
            const tbody = document.getElementById("resultBody");
            const rows = Array.from(tbody.getElementsByTagName("tr"));

            rows.sort((a, b) => {
                const scoreA = parseInt(a.getElementsByTagName("td")[1].innerText);
                const scoreB = parseInt(b.getElementsByTagName("td")[1].innerText);
                return scoreA - scoreB;
            });
            
            tbody.innerHTML = '';
            rows.forEach(row => {
                tbody.appendChild(row);
            });
        }