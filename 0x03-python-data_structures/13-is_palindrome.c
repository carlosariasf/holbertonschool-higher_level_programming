#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - check if linked list is palindrome
 * @head: list to check
 * Return: 1 if is a palindrome 0 if not
 *
**/
int is_palindrome(listint_t **head)
{
	listint_t *copy = *head;
	listint_t *copy2 = copy;
	listint_t *copy3 = copy2;
	int count = 1, count2 = 1, final = 0, j, i;
	if (*head != NULL)
	{
		while (copy->next != NULL)
		{
			count++;
			copy = copy->next;
		}
		if (count % 2 == 0)
		{
			count2 = count / 2;
			for (i = 1; i < count2; i++)
			{
				for (j = 1; j < count; j++)
					copy2 = copy2->next;
				if (count == i )
					break;
                count--;
				if (copy2->n == copy3->n)
					final++;
				copy3 = copy3->next;
                copy2 = *head;
				if (count == i)
					break;
			}
			if (final == count2-1)
				return (1);
			else
				return (0);
		}
		else
			return (0);
	}
	else
		return (1);
}
