function deleteClient(clientId) {
    Swal.fire({
        title: "Are you sure?",
        text: "You won't be able to undo this!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!"
      }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "Client deleted successfully!",
                icon: "success"
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = "/clients/" + clientId + "/delete";
                };
            });
        };
      });
}






//Populate 'Display Name' field on client_create.html with 'First Name' and 'Last_Name'
window.addEventListener('DOMContentLoaded', function () {
    var firstName = document.getElementById('id_first_name');
    var lastName = document.getElementById('id_last_name');
    var displayName = document.getElementById('id_display_name');

    // Event listener for input changes in 'First Name' field
    firstName.addEventListener('input', updateCombinedField);

    // Event listener for input changes in 'Last Name' field
    lastName.addEventListener('input', updateCombinedField);

    // Function to update combinedField
    function updateCombinedField() {
        displayName.value = firstName.value + ' ' + lastName.value;
    }
});

