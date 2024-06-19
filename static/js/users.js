window.addEventListener('DOMContentLoaded', function() {
    var userFilter = document.getElementById('user-filter-select');

    userFilter.addEventListener('change', updateUserFilter);

    function updateUserFilter() {
        if (userFilter.value == 'active') {
            window.location.href = "/users?filter=active";
        } else if (userFilter.value == 'inactive') {
            window.location.href = "/users?filter=inactive";
        } else {
            window.location.href = "/users";
        }
    };
});