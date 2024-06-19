
// Check for marker left by adding communication, if true take user back to the communications tab
window.onload = function() {
    var urlParams = new URLSearchParams(window.location.search);
    var marker = urlParams.get('comms');
    if (marker === 'true') {
        // Get tab ID and simulate click
        var communicationsTabButton = document.getElementById('nav-communications-tab');
        if (communicationsTabButton) {
            communicationsTabButton.click();
        }
    }
};

window.addEventListener('DOMContentLoaded', function() {
    var caseFilter = document.getElementById('case-filter-select');

    caseFilter.addEventListener('change', updateCaseFilter);

    function updateCaseFilter() {
        if (caseFilter.value == 'open') {
            window.location.href = "/cases?filter=open";
        } else if (caseFilter.value == 'closed') {
            window.location.href = "/cases?filter=closed";
        } else {
            window.location.href = "/cases";
        }
    };
});




function deleteCase(caseId, caseNo) {
    Swal.fire({
        title: "Delete case " + caseNo + "?",
        text: "You won't be able to undo this!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!"
      }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "Case deleted successfully!",
                icon: "success"
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = "/cases/" + caseId + "/delete";
                };
            });
        };
      });
}