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


function addNewRestaurant() {

    var rest_name = document.getElementById("rest_name").value;
    var rest_loc = document.getElementById("rest_loc").value;

    if (rest_name == "" || rest_loc == ""){
    showFailPrompt();
    return;
    }

    let data = { rest_name: rest_name, restaurant_loc: rest_loc};

    // Call postData function   
        postData('http://localhost:5000/create_new',
            data, "POST");

}

function addRestAlert(){
    silverBox({
       customIcon: "/static/images/dinner.png",
       title: {
              text: "Add New Restaurant"
       },
       centerContent: true,
       text: "Enter Restaurant Information",
       footer: "<a href='#'>Need More Information?</a>",
       showCloseButton: true,
       input: [
              {
                     label: "Restaurant Name",
                     type: "text",                          
                     placeHolder: "Enter Restaurant Name",
                     id: "rest_name",                          
                     maxLength: 30
              },
              {
                     label: "Location",
                     type: "text",
                     placeHolder: "Enter Restaurant Address",
                     id: "rest_loc",   
                     hint: "Enter short address"
              }
       ],
         confirmButton: {
              text: "SAVE",
              closeOnClick: true,
              onClick : () => {
                addNewRestaurant()
              }
       },
       cancelButton: {
            text: "CANCEL",
            closeOnClick: true
       }

    })

}

function showFailPrompt(){
    alert("Operation failed.");
}