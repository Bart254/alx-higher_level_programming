// Using Jquery to toggle classes
const toggleHeader = $('DIV#toggle_header');
const header = $('header');
toggleHeader.click(() => {
  if (header.hasClass('red')) {
    header.toggleClass('red green');
  } else if (header.hasClass('green')) {
    header.toggleClass('green red');
  } else {
    header.toggleClass('red');
  }
});
