/*
    제출 이벤트를 받는다 (이벤트 핸들링)

    제출된 입력 값들을 참조한다

    로직을 구현하여 입력값에 문제가 있을 경우 이를 감지한다

    가입화면 인사를 진행한다

*/
// function(){} 같이 이름 없이 쓰는 함수는 익명함수, 익명함수는 이벤트 객체를 받아서 입력값들을 읽어들이는 일을 한다.


const form=document.getElementById("form")

form.addEventListener("submit", function(event){
    event.preventDefault() // submit의 새로고침 차단
    
    let userId = event.target.id.value
    let userPw1 = event.target.pw1.value
    let userPw2 = event.target.pw2.value
    let userName = event.target.name.value
    let userPhone = event.target.phone.value
    let userPosition = event.target.position.value
    let userGender = event.target.gender.value
    let userEmail = event.target.email.value
    let userIntro = event.target.intro.value

    // console.log(userId, userPw1, userPw2, userName, userPhone, userPosition, userGender, userEmail, userIntro)

    if(userId.length < 6){
        alert("아이디가 너무 짧습니다. 6자 이상 입력해주세요.")
        return
    }

    if(userPw1 !== userPw2){
        alert("비밀번호가 일치하지 않습니다.")
        return
    }

    // 가입이 잘 되었다! 환영!

    document.body.innerHTML = ""
    document.write(`<p>
        ${userId}님 환영합니다.<br>
        아이디 : ${userId}<br>
        이름 : ${userName}<br>
        전화번호 : ${userPhone}<br>
        원하는 직무 : ${userPosition}
    </p>`)
    
    const userInfooz = {
        Id: userId,
        password1: userPw1,
        password2: userPw2,
        name: userName,
        phone: userPhone,
        postion: userPosition,
        gender: userGender,
        email: userEmail,
        intro: userIntro,
    }

    localStorage.setItem('userInfooz', JSON.stringify(userInfooz));
    console.log('사용자 정보가 로컬 저장소에 저장되었습니다:', userInfooz);


})