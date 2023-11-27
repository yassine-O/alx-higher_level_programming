#include "lists.h"

/**
 * check_cycle - Description
 * @list: pointer
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *first;

	first = list;
	list = list->next;
	while (list != NULL)
	{
		if (list == first)
			return (1);

		list = list->next;
	}

	return (0);
}
