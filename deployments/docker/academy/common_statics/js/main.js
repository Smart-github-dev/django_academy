// Cleaning other checkbox if the user selected one
function selectOnlyThis(id){
    var myCheckbox = document.getElementsByClassName('subscription-plans')
    Array.prototype.forEach.call(myCheckbox,function(el){
        el.checked          = false;
    });
    id.checked = true;
}

// Making sure that user select at least one check box
function atLeastOneCheckboxIsChecked(){
    const checkboxes = Array.from(document.getElementsByClassName('subscription-plans'));
    return checkboxes.reduce((acc, curr) => acc || curr.checked, false);
}


// Getting selected plan data
function getSelectedPlan() {
    var selectedPlanId  =  document.getElementById('selectedPlanId');
    var myCheckbox = document.getElementsByClassName('subscription-plans')
    Array.prototype.forEach.call(myCheckbox,function(el){
        if(el.checked) {
        selectedPlanId.value = el.id
        }
    });
}


// Make sure user select paid version of the plans
function alertForFreePlan() {
    console.log('Example')
}


// When form is submited for the subscription all other functions will be executed!!
function makeSureUserAgreed() {
    if (!atLeastOneCheckboxIsChecked()) {
        alert('Please select one of the subscription!!');
        return false;
    }

    getSelectedPlan()

    if(document.getElementById('agree').checked) {
        return true;
    } else {
        alert('Please indicate that you have read and agree to the Terms and Conditions and Privacy Policy');
        return false;
    }
}

// Get the element with id="defaultOpen" and click on it
// document.getElementById("defaultOpen").click();
