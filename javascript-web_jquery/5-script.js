$(document).ready(function () {
    // Wait for the DOM content to be fully loaded
    $('#add_item').click(function () {
      // Create a new <li> element with the text "Item"
      const newItem = $('<li>').text('Item');
  
      // Append the new <li> element to UL.my_list
      $('ul.my_list').append(newItem);
    });
  });
