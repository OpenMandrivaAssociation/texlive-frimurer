Name:		texlive-frimurer
Version:	56704
Release:	1
Summary:	Access to the 'frimurer' cipher for use with LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/frimurer
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frimurer.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frimurer.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frimurer.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides access to the 'frimurer' cipher for use
with LaTeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/fonts/frimurer
%{_texmfdistdir}/tex/latex/frimurer
%{_texmfdistdir}/fonts/type1/public/frimurer
%{_texmfdistdir}/fonts/tfm/public/frimurer
%{_texmfdistdir}/fonts/enc/dvips/frimurer
%{_texmfdistdir}/fonts/afm/public/frimurer
%doc %{_texmfdistdir}/doc/fonts/frimurer

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
