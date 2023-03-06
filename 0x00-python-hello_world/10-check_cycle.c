#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a list
 * @list: structured list
 * Return: 1 if there is a cycle, 0 if none
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	for (; list; list = list->next)
	{
		for (temp = list->next; temp; temp = temp->next)
		{
			if (temp->n == list->n)
				return (1);
		}
	}
	return (0);
}
