$(document).ready(function(){
  $('#submit').click(function(e){
    e.preventDefault()

    var formData = {
               'inputName' : $('input[name=inputName]').val(),
               'inputEmail': $('input[name=inputEmail]').val(),
               'textAreaComments': $('textArea').val()
           };

    $.ajax({
      url:$SCRIPT_ROOT + '/contact',
      data: formData,
      type: 'post',
      success: function(resp){
      alert(JSON.stringify(resp));

      }


    })
  })

});
