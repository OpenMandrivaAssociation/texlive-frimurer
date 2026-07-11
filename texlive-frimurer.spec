%global tl_name frimurer
%global tl_revision 56704

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1
Release:	%{tl_revision}.1
Summary:	Access to the frimurer cipher for use with LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/frimurer
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/frimurer.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/frimurer.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/frimurer.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides access to the 'frimurer' cipher for use with
LaTeX.

