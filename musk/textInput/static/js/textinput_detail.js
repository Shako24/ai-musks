// Array added for the Elements of the text page
const counters = [
    {value: 'HeadingCheckbox', value2: "HeadingDiv", value3:"HeadingTextbox" },
    {value: 'CheckboxCheckbox', value2: 'CheckboxDiv', value3: 'CheckboxTextbox'},
    {value: 'NavbarCheckbox', value2: 'NavbarDiv', value3: 'NavbarTextbox'},
    {value: 'DropdownCheckbox', value2: 'DropdownDiv', value3: 'DropdownTextbox'},
    {value: 'TextboxCheckbox', value2: 'TextboxDiv', value3: 'TextboxTextbox'},
    {value: 'FooterCheckbox', value2: 'FooterDiv', value3: 'FooterTextbox'},
    {value: 'ParagraphCheckbox', value2: 'ParagraphDiv', value3: 'ParagraphTextbox'},
    {value: 'LabelCheckbox', value2: 'LabelDiv', value3: 'LabelTextbox'},
    {value: 'ImageCheckbox', value2: 'ImageDiv', value3: 'ImageTextbox'},
    {value: 'TextareaCheckbox', value2: 'TextareaDiv', value3: 'TextareaTextbox'},
    {value: 'ButtonCheckbox', value2: 'ButtonDiv', value3: 'ButtonTextbox'},
    {value: 'LinkCheckbox', value2: 'LinkDiv', value3: 'LinkTextbox'}
]

// Increament function of the elemnents  
function CounterIncrement(index) {
    var i = document.getElementById(counters[index].value3).value
    document.getElementById(counters[index].value3).value = ++i;
}

// Decrement function of the elements
function CounterDecrement(index) {
    var i = document.getElementById(counters[index].value3).value
    document.getElementById(counters[index].value3).value = --i;
}

// Reset the value of all the counters
function CounterReset() {
    counters.map(c => {
        const checkbox = document.getElementById(c.value);
        const box = document.getElementById(c.value2);
        const textbox = document.getElementById(c.value3);
        
        checkbox.checked = false;
        textbox.value = 0;
        box.style.visibility = 'hidden';
    })
}


// The element button functionality for showing the counters
for (let index = 0; index < counters.length; index++) {
    const checkbox = document.getElementById(counters[index].value);
    const box = document.getElementById(counters[index].value2);
    checkbox.addEventListener('click', function handleClick() {
        if (checkbox.checked) {
            box.style.visibility = 'visible';
        } else {
            box.style.visibility = 'hidden';
        }
    });

    
}

