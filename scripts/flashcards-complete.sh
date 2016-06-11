_flashcards_completion() {
    
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}" 

    #
    #  Custom completion on `flashcards sets select` command.
    #
    opts="flashcards sets select"
    
    case "${prev}" in
        select)

            local names=$(for x in `ls ~/.flashcards/studysets/* | xargs -n 1 basename `; do echo ${x} ; done )
            COMPREPLY=( $(compgen -W "${names}" -- ${cur}) )
            return 0
            ;;
    esac

    COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
                   _FLASHCARDS_COMPLETE=complete $1 ) )

    return 0
}

complete -F _flashcards_completion -o default flashcards;
