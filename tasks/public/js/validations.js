const validateStringOnChange = (value, name, validationField ,isRequired, min, max, containSpace, containNumeric, containSymbolsCharacters, symbol) => {
    let message = "";
    if(isRequired){
        if(value.trim() == ""){
            message = `${name} is required`;
        }else if(containSpace && containNumeric && containSymbolsCharacters) {
            if(!value.trim().match(`(^[^*&^%$#@!~+-=?؟])([A-Za-z\s0-9${symbol}])+$`)){
                message = `${name} should contain english characters or numbers or ${symbol}`;
            }else if(value.length < min || value.length > max){
                message = `${name} should be between ${min} and ${max}`;
            }else {
                message = "";
            }
        }else if(containSpace && !containNumeric && containSymbolsCharacters) {
            if(!value.trim().match(`^[^*&^%$#@!~+-=?؟][A-Za-z\s ${symbol}]+$`)){
                message = `${name} should contain english character with ${symbol} as a sperator`;
            }else if(value.length < min || value.length > max){
                message = `${name} should be between ${min} and ${max}`;
            }else {
                message = "";
            }
        }else if(containSpace && !containNumeric && !containSymbolsCharacters){
            if(!value.trim().match(/^[A-Za-z\s]+$/)){
                message = `${name} should contain only english character`;
            }else if(value.length < min || value.length > max){
                message = `${name} should be between ${min} and ${max}`;
            }else {
                message = "";
            }    
        }else if(containSpace && containNumeric && !containSymbolsCharacters) {
            if(!value.trim().match(/^[A-Za-z\s0-9]+$/)){
                message = `${name} should contain english character or numbers`;
            }else if(value.length < min || value.length > max){
                message = `${name} should be between ${min} and ${max}`;
            }else {
                message = "";
            }
        }else if(!containSpace && !containNumeric && !containSymbolsCharacters) {
            if(!value.trim().match(`[A-Za-z]+$`)){
                message = `${name} should contain english character without spaces`;
            }else if(value.length < min || value.length > max){
                message = `${name} should be between ${min} and ${max}`;
            }else {
                message = "";
            }
        }else if(!containSpace && containNumeric && !containSymbolsCharacters) {
            if(!value.trim().match(`[A-Za-z]+$`)){
                message = `${name} should contain english character or numbers without spaces`;
            }else if(value.length < min || value.length > max){
                message = `${name} should be between ${min} and ${max}`;
            }else {
                message = "";
            }
        }
    }else {
        if(value.trim() == "") {
            message = ""
        }else if(containSpace && containNumeric && containSymbolsCharacters) {        
            if(!value.trim().match(`(^[^*&^%$#@!~+-=?؟])([A-Za-z\s0-9${symbol}])+$`)){
                message = `${name} should contain english characters or numbers or ${symbol}`;
            }else if(value.length < min || value.length > max){
                message = `${name} should be between ${min} and ${max}`;
            }else {
                message = "";
            }
        }else if(containSpace && !containNumeric && containSymbolsCharacters) {
            if(!value.trim().match(`^[^*&^%$#@!~+-=?؟][A-Za-z\s${symbol}]+$`)){
                message = `${name} should contain english character or ${symbol}`;
            }else if(value.length < min || value.length > max){
                message = `${name} should be between ${min} and ${max}`;
            }else {
                message = "";
            }
        }else if(containSpace && !containNumeric && !containSymbolsCharacters){
            if(!value.trim().match(`[A-Za-z\s]+$`)){
                message = `${name} should contain only english character`;
            }else if(value.length < min || value.length > max){
                message = `${name} should contain english character or ${symbol}`;
            }else {
                message = "";
            }
        }else if(containSpace && containNumeric && !containSymbolsCharacters) {
            if(!value.trim().match(`[A-Za-z\s0-9]+$`)){
                message = `${name} should contain english character or numbers`;
            }else if(value.length < min || value.length > max){
                message = `${name} should be between ${min} and ${max}`;
            }else {
                message = "";
            }
        }else if(!containSpace && !containNumeric && !containSymbolsCharacters) {
            if(!value.trim().match(`[A-Za-z]+$`)){
                message = `${name} should contain english character without spaces`;
            }else if(value.length < min || value.length > max){
                message = `${name} should contain only english character`;
            }else {
                message = "";
            }
        }else if(!containSpace && containNumeric && !containSymbolsCharacters) {
            if(!value.trim().match(`[A-Za-z]+$`)){
                message = `${name} should contain english character or numbers without spaces`;
            }else if(value.length < min || value.length > max){
                message = `${name} should be between ${min} and ${max}`;
            }else {
                message = "";
            }
        }
    }
    validationField.innerHTML = message
}


const validateEmailOnChange = (value, validationField, isRequired) => {
    let message = "";
    if(isRequired) {
        if(value.trim() == "") {
            message = "Email is required"
        }else if(!value.trim().match(
            /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          )) {
              message = "Email is not valid"
          }
    }else {
       if(value.trim() == ""){
           message = ""
       }else if(!value.trim().match(
            /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          )) {
            message = "Email is not valid"
        } else {
            message = ""
        }
    }
    validationField.innerHTML = message
}


const validatePasswordOnChange = (value, validationField, min, max) => {
    let message = "";
    if(value.trim() == ""){
        message = `Password is required`;
    }else {
        if(!value.trim().match(/^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*?&#])([a-zA-Z0-9@$!%*?&#])+$/)){
            message = `Password should contain at least one uppercase, lowercase, number, and special characters`;
        }else if(value.length < min || value.length > max){
            message = `Password should be between ${min} and ${max}`;
        }else {
            message = "";
        }
    }

    validationField.innerHTML = message
}

const validateNumeric = (value, name, validationField , isRequired) => {
    let message = ""
    if(isRequired){
        if(value.trim() != "") {
            message = `${name} is required`
        }else if(!value.trim().match(/^[0-9]+$/)){
            message = `${name} should contain only numeric values`
        }else {
            message = ""
        }
    }else{
        if(!value.trim().match(/^[0-9]+$/)){
            message = `${name} should contain only numeric values`
        }else {
            message = ""
        }
    }
    validationField.innerHTML = message
}