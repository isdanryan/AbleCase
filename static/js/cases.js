function deleteCase(caseId) {
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