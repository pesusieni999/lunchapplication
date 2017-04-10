/**
 * Delete topic.
 * Reads DELETE URL from DOM.
 * Will redirect the user to lunch application main page.
 */
function deleteTopic() {
    $.ajax({
        url: $(".topic-delete-link").attr("href"),
        type: "DELETE",
        beforeSend: function(xhr) {
            if (!this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", $("[name='csrfmiddlewaretoken']").val());
            }
        }
    })
    .done(function() {
        // Redirect since current page is no longer valid.
        window.location.replace($("#deleteRedirect").attr("href"));
    })
    .fail(function() {
        return alert("Failed to delete topic.\n\nPlease reload the page and try again.");
    });
}

function deleteComment(deleteURL) {
    $.ajax({
        url: deleteURL,
        type: "DELETE",
        beforeSend: function(xhr) {
            if (!this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", $("[name='csrfmiddlewaretoken']").val());
            }
        }
    })
    .done(function() {
        // Redirect since current page is no longer valid.
        location.reload(true);
    })
    .fail(function() {
        return alert("Failed to delete comment.\n\nPlease reload the page and try again.");
    });
}

/**
 * Update topic.
 * Reads new topic name, topic text and update URL from DOM.
 * If successful, will reload the page.
 */
function updateTopic() {
    var newName = $("#new-topic-name").val().toString();
    var newText = $("#new-topic-text").val().toString();

    $.ajax({
        url: $(".topic-edit-link").attr("href"),
        type: 'POST',
        data: {
            name: newName,
            text: newText
        },
        beforeSend: function(xhr) {
            if (!this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", $("[name='csrfmiddlewaretoken']").val());
            }
        }
    })
    .done(function() {
        // Reload the page to get up to date data from server.
        // This could be improved so that instead of reload, we get new data from server in JSON
        // and write it directly to DOM.
        location.reload(true);
    })
    .fail(function() {
        return alert("Failed to update the topic.\n\nPlease reload the page and try again.");
    });
}

function updateComment() {
    var newText = $("#new-comment-text").val().toString();

    $.ajax({
        url: $("#comment-form").attr("action"),
        type: 'POST',
        data: {
            text: newText
        },
        beforeSend: function(xhr) {
            if (!this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", $("[name='csrfmiddlewaretoken']").val());
            }
        }
    })
    .done(function() {
        // Reload the page to get up to date data from server.
        // This could be improved so that instead of reload, we get new data from server in JSON
        // and write it directly to DOM.
        location.reload(true);
    })
    .fail(function() {
        return alert("Failed to update the topic.\n\nPlease reload the page and try again.");
    });

    // Clear the dialog so that if user tries to create new comment, it is empty.
    $("#new-comment-text").val("");
    $("#comment-form").attr("action", $("#postNewCommentUrl").attr("href"));
}

/**
 * Open Topic edit-dialog.
 * Update dialog form fields to current text values.
 * @param modalDlg: Modal dialog DOM element.
 */
function updateTopicLinkClicked(modalDlg) {
    $("#new-topic-name").val($("#topic-name").text());
    $("#new-topic-text").val($("#topic-text").text());
    modalDlg.modal({
        keyboard: true
    });
}

function updateCommentLinkClicked(modalDlg, text, url) {
    $("#new-comment-text").val(text);
    $("#comment-form").attr("action", url);
    modalDlg.modal({
        keyboard: true
    });
}

$(document).ready(function() {
    $(".topic-delete-link").click(function(e) {
        e.preventDefault();
        deleteTopic();
    });

    $(".comment-delete-link").click(function(e) {
        e.preventDefault();
        deleteComment($(this).attr("href"));
    });

    $(".topic-edit-link").click(function(e) {
        e.preventDefault();
        updateTopicLinkClicked($("#edit-topic-modal"));
    });

    $(".comment-edit-link").click(function(e) {
        e.preventDefault();
        var currentText = $(this).parent().parent().find(".comment-text-field").text().toString();
        updateCommentLinkClicked($("#comment-modal"), currentText, $(this).attr("href"));
    });

    $("#update-topic-btn").click(function(e) {
        e.preventDefault();
        updateTopic();
    });

    $("#comment-submit").click(function(e) {
        e.preventDefault();
        updateComment();
    });

    $("#comment-dlg-dismiss").click(function(e) {
        // Clear the dialog so that if user tries to create new comment, it is empty.
        $("#new-comment-text").val("");
        $("#comment-form").attr("action", $("#postNewCommentUrl").attr("href"));
    })
});