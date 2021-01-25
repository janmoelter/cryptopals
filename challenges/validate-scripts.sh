#!/bin/bash

set -o nounset

clear

echo '================================================================================'
echo ' CRYPTOPALS CHALLENGES :: UNIT TEST'
echo '================================================================================'

for n in {01..56}; do
	CHALLENGE_N_PY="challenge-${n}.py"
	if [[ -e ${CHALLENGE_N_PY} ]]; then
		./${CHALLENGE_N_PY} > /dev/null
		R=$?

		echo -n "Challenge $n: "
	
		if [[ $R == 0 ]]; then
			echo "✔️  Pass."
		else
			echo "❌  Fail."
		fi
	fi

done
