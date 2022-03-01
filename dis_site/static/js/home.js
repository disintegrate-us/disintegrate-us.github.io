$('img').contextmenu(function() {
    return false;
});

$('img').on('dragstart', function(event) { event.preventDefault(); });