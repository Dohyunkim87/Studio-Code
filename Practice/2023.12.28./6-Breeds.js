const apiRandomdogs = "https://dog.ceo/api/breeds/image/random/42"
const apiAllBreeds = "https://dog.ceo/api/breeds/list/all"
const request1 = new XMLHttpRequest()
const request2 = new XMLHttpRequest()

const header = document.getElementById("header")
const main = document.getElementById("main")
const input = document.getElementById("filter-text")
const button = document.getElementById("filter-button")
const select = document.getElementById("filter-select")

const currentDogs = []

function displayDogs(item){
    const dogImgDiv = document.createElement("div")
    dogImgDiv.classList.add("flex-item")
    dogImgDiv.innerHTML = `
        <img src=${item}>
    `
    main.appendChild(dogImgDiv)
}

window.addEventListener("load", function(){
    // 강아지 사진 뿌리기
    request1.open("get", apiRandomdogs)
    request1.addEventListener("load", function(){
        const response = JSON.parse(request1.response)
        response.message.forEach(function(item){
            currentDogs.push(item)
            displayDogs(item)
        })
    })
    request1.send()

    // 셀렉트에 견종정보 뿌리기
    request2.open("get", apiAllBreeds)
    request2.addEventListener("load", function(){
        const response = JSON.parse(request2.response)
        Object.keys(response.message).forEach(function(item){
            const option = document.createElement("option")
            option.textContent = item
            option.value = item
            select. appendChild(option)
        })
    })
    request2.send()
})

button.addEventListener("click",function(){
    main.innerHTML = ""
    let filteredDogs = currentDogs.filter(function(item){
        return item.indexOf(input.value) !== -1
    })

    input.value = ""

    filteredDogs.forEach(function(item){
        displayDogs(item)
    })
})

select.addEventListener("change",function(){
    main.innerHTML = ""
    let filteredDogs = currentDogs.filter(function(item){
        return item.indexOf(select.value) !== -1
    })

    filteredDogs.forEach(function(item){
        displayDogs(item)
    })
})

more.addEventListener("click",function(){
    request1.open("get", apiRandomdogs)
    request1.addEventListener("load",function(){
        const response = JSON.parse(request1.response)
        response.message.forEach(function(item){
            currentDogs.push(item)
            displayDogs(item)
    })
})
    request1.send()
})

tothetop.addEventListener("click",function(){
    // scrollTo : 주어진 위치로 스크롤을 이동한다.
    window.scrollTo({top:0})
})

reset.addEventListener("click", function () {
    // 모든 필터링된 내용 초기화
    main.innerHTML = "";

    // 새로운 강아지 사진 가져오기
    request1.open("get", apiRandomdogs);
    request1.addEventListener("load", function () {
        const response = JSON.parse(request1.response);
        response.message.forEach(function (item) {
            currentDogs.push(item);
            displayDogs(item);
        });
    });
    request1.send();
})