var music = document.getElementById('am-nhac');
music.addEventListener('click', function() {
    var x = document.getElementById('off-music').style.display;
    if (x == 'none') {
        document.getElementById("on-music").style.display = 'none';
        document.getElementById("off-music").style.display = 'inline-block';
        $('#audio').attr('src', '');
        console.log(document.getElementById("doam").selected);
    } else {
        document.getElementById("on-music").style.display = 'inline-block';
        document.getElementById("off-music").style.display = 'none';
        $('#audio').attr('src', './static/thong1.mp3');
    }
}, false);

function getSelectedValue() {
    var a = document.getElementById("selectedValueNe");
    var selectedValue = a.options[a.selectedIndex].id;
    document.getElementById("form-cal").action = "/do/" + selectedValue
    return selectedValue;
}

const form = document.getElementById('form-cal');
console.log(form);

form.addEventListener('submit', (e) => {
    var form_data = new FormData();
    var ins = document.getElementById("fileInput").files.length;
    if (ins == 0) {
        Alert.render('File đưa vào không được để trống!')
    } else {
        var file_name = document.getElementById("fileInput").files[0].name;
        let stack = [];
        let extension = "";
        for (var i = file_name.length - 1; i >= 0; i--) {
            if (file_name[i].charCodeAt() - 46 == 0) {
                stack.push(file_name[i]);
                break;
            } else {
                stack.push(file_name[i]);
            }
        }
        while (stack.length > 0) {
            extension += stack.pop();
        }
        if (extension == ".csv") {
            if (getSelectedValue() == "null") {
                Alert.render("Hãy chọn điều kiện mong muốn!");
            } else return;
        } else {
            Alert.render("File đưa vào phải là file .csv !");
        }
    }
    e.preventDefault();
})

function CustomAlert() {
    this.render = function(dialog) {
        var winW = window.innerWidth;
        var winH = window.innerHeight;
        var dialogoverlay = document.getElementById('dialogoverlay');
        var dialogbox = document.getElementById('dialogbox');
        dialogoverlay.style.display = "block";
        dialogoverlay.style.height = winH + "px";
        dialogbox.style.left = (winW / 2) - (550 * .5) + "px";
        dialogbox.style.top = "30%";
        dialogbox.style.display = "block";
        document.getElementById('dialogboxhead').innerHTML = "Lỗi!";
        document.getElementById('dialogboxbody').innerHTML = dialog;
        document.getElementById('dialogboxfoot').innerHTML = '<button onclick="Alert.ok()">Exit</button>';
    }
    this.ok = function() {
        document.getElementById('dialogbox').style.display = "none";
        document.getElementById('dialogoverlay').style.display = "none";
    }
}
var Alert = new CustomAlert();