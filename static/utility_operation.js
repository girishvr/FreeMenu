// utility_operation.js
// All the operations that are reused

function postData(path, params, method) {
  
    // Create form
    const hidden_form = document.createElement('form');

    // Set method to post by default
    hidden_form.method = method || 'POST';
      
    // Set path
    hidden_form.action = path;
      
    for (const key in params) {
        if (params.hasOwnProperty(key)) {
            const hidden_input = document.createElement
                ('input');
            hidden_input.type = 'hidden';
            hidden_input.name = key;
            hidden_input.value = params[key];

            hidden_form.appendChild(hidden_input);
        }
    }

    document.body.appendChild(hidden_form);
    hidden_form.submit();
}


function showFailPrompt(){
    alert("Operation failed.");
}