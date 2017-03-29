function initDataTables() {
    $(".datatables-table").each(function() {
        var initData = {
            "paging": true,
            "ordering": true,
            "order": [[ 3, "desc" ]],
            "language": {
                "sProcessing":      "Processing...",
                "sLengthMenu":      "Show _MENU_ entries",
                "sZeroRecords":     "No matching records found",
                "sInfo":            "Showing _START_ to _END_ of _TOTAL_ entries",
                "sInfoEmpty":       "Showing 0 to 0 of 0 entries",
                "sInfoFiltered":    "filtered from _MAX_ total entries",
                "sInfoPostFix":     "",
                "sSearch":          "Search:",
                "sUrl":             "",
                "oPaginate": {
                    "sFirst":       "First",
                    "sPrevious":    "Previous",
                    "sNext":        "Next",
                    "sLast":        "Last"
                }
            }
        };
        $(this).DataTable(initData);
    });
}

$(document).ready(function() {
   initDataTables();
});