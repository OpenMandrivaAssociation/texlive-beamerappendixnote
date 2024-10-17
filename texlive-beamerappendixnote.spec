Name:		texlive-beamerappendixnote
Version:	55732
Release:	2
Summary:	Create notes on appendix frames in beamer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamerappendixnote
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerappendixnote.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerappendixnote.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerappendixnote.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package introduces the \appxnote command, which puts the
note's content on a separate beamer frame shown by the command
\printappxnotes. It also creates interactive buttons to move
back and forth between the two frames.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/beamerappendixnote
%{_texmfdistdir}/tex/latex/beamerappendixnote
%doc %{_texmfdistdir}/doc/latex/beamerappendixnote

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
