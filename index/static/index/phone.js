const phoneForm = document.getElementById('phone-form');
const phoneInput = document.getElementById('phone-input');
const addButton = document.getElementById('add-button');
const phoneList = document.getElementById('phone-list');
const csrf = Cookies.get('csrftoken');

const messageForm = document.getElementById('message-form');
const messageInput = document.getElementById('input-form-message');
const addMessage = document.getElementById('add-message');
const sendMessage = document.getElementById('send-message')
addButton.addEventListener('click', () => {
  const phoneNumber = phoneInput.value.trim();
  console.log("This is the added value", phoneNumber)
  if (phoneNumber !== '') {
    addPhoneNumber(phoneNumber);
    phoneInput.value = '';
  }
});

function addPhoneNumber(phoneNumber) {
  console.log("This is the added value", phoneNumber)
  fetch('phone', {
    method: "POST",
    headers: {'X-CSRFToken': csrf},
    body: JSON.stringify({
        "phone": phoneNumber,
      
    })
    // .then(() => location.reload())
    
})


// window.reload()
}

if(document.querySelector("#link-delete")){
    document.querySelector("#link-delete").addEventListener("click", () => {
        if(window.confirm("Are you sure? This action CANNOT be undone.")){
            fetch(`phone/${this.dataset.id}`, {
                method: "DELETE",
                headers: {'X-CSRFToken': csrf},
            })
            .then(() => {
                document.querySelectorAll(".question").forEach(q =>{
                    if(q.dataset.id === this.dataset.id){
                        q.parentNode.removeChild(q)
                    }
                })
            })
        }
    })
}


addMessage.addEventListener('click', () => {
    const message = messageInput.value.trim();
    console.log("This is the added message", message)
    if (message !== '') {
      addNewMessage(message);
      phoneInput.value = '';
    }
  });
  
  function addNewMessage(message) {
    console.log("This is the added message", message)
    fetch('message', {
      method: "POST",
      headers: {'X-CSRFToken': csrf},
      body: JSON.stringify({
          "message": message,
        
      })
      
  })
  
  
  // window.reload()
  }

  sendMessage.addEventListener('click', () => {
    fetch('send_message', {
        method: "POST",
        headers: {'X-CSRFToken': csrf},
        
    })
 
  });