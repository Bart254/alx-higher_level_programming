// Using Jquery to set an event
const redHeader = $('DIV#red_header');
const header = $('header');
redHeader.click(() => {
  header.addClass('red');
});
