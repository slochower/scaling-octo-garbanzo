function includes(tbl, x)
  for _, y in ipairs(tbl) do
      if y == x then return true end
  end
  return false
end

function Span(el) 
if el.classes:includes('red') and FORMAT == 'latex' then 
  return { pandoc.RawInline('latex', '\\textcolor{red}{'),
           el, pandoc.RawInline('latex', '}') }
end 
end

function Span(el) 
  if el.classes:includes('Maroon') and FORMAT == 'latex' then 
    return { pandoc.RawInline('latex', '\\textcolor{Maroon}{'),
             el, pandoc.RawInline('latex', '}') }
  end 
  end