
//Populate 'Display Name' field on client_create.html with 'First Name' and 'Last_Name'
window.addEventListener('DOMContentLoaded', function () {
    const now = new Date();

    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');

    const dateTimeInteger = `${year}${month}${day}${hours}${minutes}${seconds}`;

    var firstName = document.getElementById('id_first_name');
    var lastName = document.getElementById('id_last_name');
    var displayName = document.getElementById('id_display_name');
    var clientReference = document.getElementById('id_client_reference');

    var clientFilter = document.getElementById('client-filter-select');

    // User firstName to check if we are on the client_details.html page
    if (firstName) {
        // Event listener for input changes in 'First Name' field
        firstName.addEventListener('input', updateCombinedField);

        // Event listener for input changes in 'Last Name' field
        lastName.addEventListener('input', updateCombinedField);

        // Function to update combinedField
        function updateCombinedField() {
            displayName.value = firstName.value + ' ' + lastName.value;
            clientReference.value = displayName.value.charAt(0).toUpperCase() + dateTimeInteger;
        };
    };

    // USer clientFilter to check if we are on the client_list.html page
    if (clientFilter) {

        // Event listener for client filter
        clientFilter.addEventListener('change', updateClientFilter);


        function updateClientFilter() {
            if (clientFilter.value == 'active') {
                window.location.href = "/clients?filter=active";
            } else if (clientFilter.value == 'inactive') {
                window.location.href = "/clients?filter=inactive";
            } else {
                window.location.href = "/clients";
            }
        };
    };

});