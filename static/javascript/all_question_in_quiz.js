$(document).ready(function(){
    // const opt = $('#id_is_multiple_correct').val();
});
let opt = $('#id_is_multiple_correct');
let choice = $(".choice");
let f=0;

// function uncheck(curr) {
//     choice.prop('checked', false).not(curr);
//
// }


opt.change(function (){
    // alert('hello');
    if (this.checked){
        // $('#id_is_ans_option_1').attr('checked', 'unchecked');
        f=1;
    }
    else{
        // $('#id_is_ans_option_1').removeAttr('checked');
             choice.prop('checked', false);
             f=0;
    }
})


$('#id_is_ans_option_1').change(function () {
    if (f === 0){
        $('.choice').not(this).prop('checked', false);
    }

})
$('#id_is_ans_option_2').change(function () {
    if (f === 0){
        $('.choice').not(this).prop('checked', false);
    }

})
$('#id_is_ans_option_3').change(function () {
    if (f === 0){
        $('.choice').not(this).prop('checked', false);
    }

})
$('#id_is_ans_option_4').change(function () {
    if (f === 0){
        $('.choice').not(this).prop('checked', false);
    }

})




// const btn = $('#submit')
// const span = $("#close");
// const modal = $("#modal-question")
// btn.click(function (){
//     modal.css('display', 'block');
// })
// span.onclick = function() {
//     modal.css('display', 'none');
// }
// window.onclick(function(e){
//     modal.style.display = "none";
// })