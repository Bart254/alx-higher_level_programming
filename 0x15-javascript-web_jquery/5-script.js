// Adding items into elements
const divList = $('DIV#add_item');
const list = $('ul');
const newElement = '<li>Item</li>';
divList.click(() => {
  list.append(newElement);
});
