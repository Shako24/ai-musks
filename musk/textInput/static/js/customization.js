// References
// https://www.w3schools.com/howto/howto_js_element_iframe.asp
// https://stackoverflow.com/questions/9249680/how-to-check-if-iframe-is-loaded-or-it-has-a-content


// This functions load when the Page is loaded
document.addEventListener('DOMContentLoaded', function (event) {
    document.getElementById('output_frame').addEventListener('load', function() { // Iframe load function
        console.log('The iframe has loaded!');
        count = 1;
        const elem = "elem";
        // Assigns the onClick function to Iframe element
        while (document.getElementById('output_frame').contentWindow.document.getElementById(elem+String(count)) != null) {
            document.getElementById('output_frame').contentWindow.document.getElementById(elem+String(count)).addEventListener("click", onClick);
            console.log('elem configured');
            count += 1;
        }
        // Assigns the onClick function to Iframe element
        count = 0;
        const elemelem = "elemelem";
        while (document.getElementById('output_frame').contentWindow.document.getElementById(elemelem+String(count)) != null) {
            document.getElementById('output_frame').contentWindow.document.getElementById(elemelem+String(count)).addEventListener("click", onClick);
            console.log('elemelem configured');
            count += 1;
        }
    })
})

var button = document.getElementById('button').addEventListener("click", clicked); // onClick added for for make changes button
var download_button = document.getElementById('download_button').addEventListener("click", downloadClick); // onClick added for download button
var frame = document.getElementById('output_frame'); // Iframe stored in the variable

// onClick function for Iframe element 
function onClick(e) {
    e.preventDefault()
    console.log(e.target.id, 'clicked')
    const cusinput = window.top.document.getElementById("custom_input");
    const cusoption = window.top.document.getElementById("custom_option");
    cusinput.value = e.target.id;
    console.log(e.target.tagName);
    // console.log(e.target.className)
    if ( e.target.className == 'topnav') { // Options altered when Navbar is clicked
        cusoption.options[1].style.display = 'block';
        cusoption.options[2].style.display = 'none';
        cusoption.options[3].style.display = 'none';
    }
    else if (e.target.tagName == 'IMG') { // Options altered when img is clicked
        cusoption.options[1].style.display = 'none';
        cusoption.options[2].style.display = 'none';
        cusoption.options[3].style.display = 'none';
    }
    else { // All options shown when other elements are clicked
        cusoption.options[1].style.display = 'block';
        cusoption.options[2].style.display = 'block';
        cusoption.options[3].style.display = 'block';
    }
}

// Download functionality 
function downloadClick(e) {
    e.preventDefault();
    let newelement = frame.contentWindow.document;
    let head = newelement.head.outerHTML;
    let body = newelement.body.outerHTML;
    let h1 = document.getElementById('header1');
    const file = new File(["<!DOCTYPE html>\n<html>\n"+head+'\n'+body+"\n"], String(h1.innerHTML)+".html", {
        type: "html,charset=utf-8"
      });
      saveAs(file);
      


}

// Make Change button Functionality
function clicked(e) {
    e.preventDefault()
    const element_id = document.getElementById("custom_input").value;
    const option = document.getElementById("custom_option").value;
    if (element_id != "") {
        let newel = frame.contentWindow.document.getElementById(element_id);
        console.log(option);
        switch (option) {
            case '1':
                newel.remove(); // element removed
                break;
            case '2':
                colorChange(newel); // Background Color change
                break;
            case '3':
                fontChange(newel); // Font Color Change
                break;
            case '4':
                textChange(newel); // Text of the Element changed
                break;
            default:
                break;
        }
    } else {
        console.log('no value selected');
    }     
}

// Background Color change
function colorChange(element) {
    const val = document.getElementById('element-color').value;
    element.style.backgroundColor = val;
}

// Font Color Change
function fontChange(element) {
    const val = document.getElementById('element-font-color').value;
    element.style.color = val;
}

// Text of the Element changed
function textChange(element) {
    const val = document.getElementById('element-text').value;
    if (element.innerHTML.indexOf('<input type="checkbox">') != -1) {
        checkboxTextChange(val, element); // Checkbox text changed
    }
    else if (element.innerHTML.indexOf('<input type="radio">') != -1) {
        radioTextChange(val, element); // Radio text changed
    }   
    else if (element.tagName == "SELECT") {
        selectTextChange(val, element); // Dropdown options changed
    }
    else {
        element.innerHTML = val;
    }
}

// Checkbox text changed
function checkboxTextChange(val, element) {
    element.innerHTML = '<input type="checkbox">'+val;
}

// Radio text changed
function radioTextChange(val, element) {
    element.innerHTML = '<input type="radio">'+val;
}

// Dropdown options changed
function selectTextChange(val, element) {
    for (let i = 0; i < element.options.length; i++) {
        element.options[i].value = val+String(i+1);
        element.options[i].textContent = val+String(i+1);
        
    }
}  

// onChange functionality when value form dropdown changed
function optionSelected() {
    let option = document.getElementById("custom_option").value;
    let val = document.getElementById('element-color');
    let val2 = document.getElementById('element-font-color');
    let val3 = document.getElementById('element-text');
    console.log(option)
    if (option == '1') {
        val.value = "";
        val2.value = "";
        val3.value = "";
        val.style.display = 'none';
        val2.style.display = 'none';
        val3.style.display = 'none';
    }
    // Shows the change background color input field
    else if (option == '2') {
        val.style.display = 'block';
        val2.style.display = 'none';
        val2.value = "";
        val3.style.display = 'none';
        val3.value = "";
    }
    // Shows the change font color input field
    else if (option =='3') {
        val2.style.display = 'block';
        val.style.display = 'none';
        val.value = "";
        val3.style.display = 'none';
        val3.value = "";
    }
    // Shows the change text input field
    else if (option == "4") {
        val3.style.display = 'block';
        val.value = "";
        val2.value = "";
        val.style.display = 'none';
        val2.style.display = 'none';
    }

}