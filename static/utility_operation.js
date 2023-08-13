// utility_operation.js
// All the operations that are reused

function postData(path, params, method) {

    console.log(path);
    
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


function SomeDeleteRowFunction(o, route) {

    silverBox({
       alertIcon: "question",
       text: "Remove the menu item?",
       centerContent: true,
       confirmButton: {
              text: "Remove",
              closeOnClick: true,
              onClick : () => {
                var p=o.parentNode.parentNode;
                p.parentNode.removeChild(p);
                console.log(o.id);
                let data = {};
                postData(route, data, "POST");                
              }
       },
       cancelButton: {
              text: "Cancel"
       }
})

    

     
}   

function addNewRestaurant() {

    // Get restaurant information from the input fields
    var rest_name = document.getElementById("rest_name").value;
    var rest_loc = document.getElementById("rest_loc").value;

    // Validation check
    if (rest_name == "" || rest_loc == ""){
        showFailPrompt();
        return;
    }

    // Parameters
    let data = { rest_name: rest_name, restaurant_loc: rest_loc};

    var base_url = window.location.origin;
    let path = base_url + "/create_new"

    // Call postData function   
    postData(path, data, "POST"); //'http://13.126.62.86:5000/create_new'

}
// SilverBox usage from the developers ://

// silverBox({
//   input: {
//     name: "saber",
//     value: "sword"
//   },
//   confirmButton: {
//     closeOnClick: false,
//     onClick: () => {
//       // Select the input (or inputs) you need
//       const saber = document.querySelector(".silverBox input[name='saber']")
      
//       // Do stuff with their values
//       console.log(saber.value);
//     },
//   },
// });


function addRestAlert(){
    var base_url = window.location.origin;

    silverBox({
       customIcon: base_url + "/static/images/dinner.png",
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