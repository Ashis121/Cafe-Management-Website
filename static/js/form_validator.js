
 const first_name = document.getElementById("first_name").value;
 const last_name = document.getElementById("last_name").value;
// const branch = document.getElementById("branch").value;
// const mobile = document.getElementById("mobile").value;
// const email = document.getElementById("email").value;
// const password = document.getElementById("password").value;
// const password2 = document.getElementById("password2").value;
// const term = document.getElementById("term");

let error = false;
//name validation
if(first_name === ""){
    //console.log("name is required");
    document.getElementById("first_name_error").innerHTML ="Name is required";
    error = true;
}
else{
    document.getElementById("first_name_error").innerHTML = "";
}
//gender validation
// if(!gender[0].checked && !gender[1].checked && !gender[2].checked){
//     document.getElementById("gender_error").innerHTML ="Please select your gender";
//     error=true;
// }
// else{
//     document.getElementById("gender_error").innerHTML ="";
// }
// //branch validation
// if(branch===""){
//     document.getElementById("branch_error").innerHTML = "Select your branch";
//     error = true;
// }
// else{
//     document.getElementById("branch_error").innerHTML = "";
// }
// //mobile validation
// if(mobile===""){
//     document.getElementById("mobile_error").innerHTML = "Please enter your mobile number";
//     error = true;
// }
// else if(mobile.length !=10 || isNaN(mobile)){
//     document.getElementById("mobile_error").innerHTML="Please enter your 10 digit mobile number"
//     error=true;

// }
// else{
//     document.getElementById("mobile_error").innerHTML = "";
// }
// //validation of email
// let atPos= email.indexOf('@');
// let dotPos=email.lastIndexOf('.'); 
// if(email===""){
//     document.getElementById("email_error").innerHTML="Email is Required";
//     error=true;
// }
// else if(atPos <=0 || dotPos<=0 || dotPos-atPos <=4 || dotPos==email.length-1){
//     document.getElementById("email_error").innerHTML="Enter a valid email id";
//     error=true;
// }
// else{
//     document.getElementById("email_error").innerHTML="";
// }
// //validation of password
// if(password===""){
//     document.getElementById("password_error").innerHTML="Enter your password";
//     error=true;
// }
// else if(password.length<8 || password.length>16){
//     document.getElementById("password_error").innerHTML="Password must contain 8-16 charecter";
//     error=true;
// }
// else if(!password.match(/[a-z]/)){
//     document.getElementById("password_error").innerHTML="Must have one numbr";
//     error=true;
// }
// else if(!password.match(/[0-9]/)){
//     document.getElementById("password_error").innerHTML="Must have one charecter";
//     error=true;
// }
// else if(!password.match(/[@#$%^&*]/)){
//     document.getElementById("password_error").innerHTML="Must have one numbr";
//     error=true;
// }
// else{
//     document.getElementById("password_error").innerHTML="";
// }
// //validation of confirm password
// if(password2===""){
//     document.getElementById("password2_error").innerHTML="Enter your password";
//     error=true;
// }
// else if(password!=password2){
//     document.getElementById("password2_error").innerHTML="Password must be same";
//     error=true;
// }
// else{
//     document.getElementById("password2_error").innerHTML="";
// }
// //validation of check bottom
//  //gender validation
//  if(!term.checked){
//     document.getElementById("term_error").innerHTML ="Please agree to these terms & conditions";
//     error=true;
// }
// else{
//     document.getElementById("term_error").innerHTML ="";
// }

// if(error){
//     return false;
// }
// else{
//     return true;
// }
// }