##
## EPITECH PROJECT, 2020
## Makefile
## File description:
## Makefile of 104intersection
##

NAME	=	104intersection

all:
	chmod +x $(NAME)

$(NAME): all

clean:
	rm -f *~
	rm -f *#

fclean: clean

re:	fclean all