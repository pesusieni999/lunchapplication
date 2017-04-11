function fetchMenu(menuDate) {
    $.ajax({
        url: "https://api.ruoka.xyz/" + menuDate,
        type: 'GET',
        dataType: "json",
        beforeSend: function(xhr) {
            if (!this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", tokenId);
            }
        }
    })
    .done(function(data) {
        //console.log(JSON.stringify(data, null, 2));

        // Clear current html.
        var menuDomElem = $("#menu-lists");
        menuDomElem.html("");

        // Construct inner HTML based on received data.
        var restaurants = data["restaurants"];
        var restaurantCount = restaurants.length;
        var innerHtml = "";

        for (var l = 0; l < restaurantCount; ++l) {
            var restaurantName = restaurants[l]["name"];
            innerHtml += "<li><ul>";

            var menus = restaurants[l]["menus"];
            var menusCount = menus.length;
            for (var l2 = 0; l2 < menusCount; ++l2) {
                var meals = menus[l2]["meals"];
                var foodPlace = menus[l2]["name"];
                innerHtml += "<li><p><b>" + restaurantName + " - " + foodPlace + "</b></p><ul>";
                var mealsCount = meals.length;
                for (var l3 = 0; l3 < mealsCount; ++l3) {
                    var mealName = meals[l3]["name"];
                    innerHtml += "<li><p><b>" + mealName + "</b></p><ul>"
                    var mealContent = meals[l3]["contents"];
                    var mealContentCount = mealContent.length;
                    for (var l4 = 0; l4 < mealContentCount; ++l4) {
                        var foodName = mealContent[l4]["name"];
                        innerHtml += "<li>" + foodName + "</li>";
                    }
                    innerHtml += "</ul></li>";
                }
                innerHtml += "</ul></li>";
            }
            innerHtml += "</ul></li>";
        }

        // Set new data to menu html.
        menuDomElem.html(innerHtml);
    })
    .fail(function() {
        return alert("Failed to retrieve menu data.\n\nPlease reload the page and try again.");
    });
}

$(document).ready(function() {
    var d = new Date();
    fetchMenu(d.toISOString().split("T")[0]);
    /*
    $("#fetch-menu-btn").click(function() {
        var d = new Date();
        fetchMenu(d.toISOString().split("T")[0]);
    });*/
});