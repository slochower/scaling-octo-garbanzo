function Span(el) 
  if el.classes[1] == 'red' then 
    return { pandoc.rawInline('tex', '\textcolor{red}{'), 
             el, pandoc.rawInline('tex', '}') }
  end 
end 

