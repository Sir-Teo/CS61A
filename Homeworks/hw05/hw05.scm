;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Mutable functions in Scheme

(define (make-fib)
  (define curr 0) (define next 1)
    (define (fib)
      (begin
        (define before curr)
        (set! curr next)
        (set! next (+ curr before))
        before
      )
    )
    fib
)
