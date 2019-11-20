##
## EPITECH PROJECT, 2019
## SEC_crypto_2019
## File description:
##  Makefile for SEC_crypto_2019
##

RM      = rm -f

NAME1    = challenge01
NAME2    = challenge02
NAME3    = challenge03
NAME4    = challenge04
NAME5    = challenge05
NAME6    = challenge06
NAME7    = challenge07
NAME8    = challenge08
NAME9    = challenge09

SRC1    = src/hex_to_base64.py
SRC2    = src/fixed_xor.py
SRC3    = src/single_byte_xor.py
SRC4    = src/detect_single_byte.py
SRC5    = src/implement_repeating_key.py
SRC6    = src/break_repeating_key.py
SRC7    = src/aes_ecb.py
SRC8    = src/detect_aes_ecb.py
SRC9    = src/implement_cbc.py

all: $(NAME1) $(NAME2) $(NAME3) $(NAME4) $(NAME5) $(NAME6) $(NAME7) $(NAME8) $(NAME9)

all: $(NAME1) $(NAME2) $(NAME3) $(NAME4) $(NAME5) $(NAME6) $(NAME7) $(NAME8) $(NAME9)

$(NAME1): $(OBJS)
	cp $(SRC1) $(NAME1)
	chmod 775 $(NAME1)

$(NAME2): $(OBJS)
	cp $(SRC2) $(NAME2)
	chmod 775 $(NAME2)

$(NAME3): $(OBJS)
	cp $(SRC3) $(NAME3)
	chmod 775 $(NAME3)

$(NAME4): $(OBJS)
	cp $(SRC4) $(NAME4)
	chmod 775 $(NAME4)

$(NAME5): $(OBJS)
	cp $(SRC5) $(NAME5)
	chmod 775 $(NAME5)

$(NAME6): $(OBJS)
	cp $(SRC6) $(NAME6)
	chmod 775 $(NAME6)

$(NAME7): $(OBJS)
	cp $(SRC7) $(NAME7)
	chmod 775 $(NAME7)

$(NAME8): $(OBJS)
	cp $(SRC8) $(NAME8)
	chmod 775 $(NAME8)

$(NAME9): $(OBJS)
	cp $(SRC9) $(NAME9)
	chmod 775 $(NAME9)

clean:
	$(RM) $(NAME1)
	$(RM) $(NAME2)
	$(RM) $(NAME3)
	$(RM) $(NAME4)
	$(RM) $(NAME5)
	$(RM) $(NAME6)
	$(RM) $(NAME7)
	$(RM) $(NAME8)
	$(RM) $(NAME9)

fclean: clean

re:     fclean all

.PHONY: all clean fclean re
